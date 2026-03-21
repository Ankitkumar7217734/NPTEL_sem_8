import os
import re

template = r"""%% ============================================================
%% Introduction to Cognitive Psychology — Week {week_num} Study Notes
%% ============================================================
\documentclass[11pt,a4paper]{{article}}

\usepackage[a4paper, left=1.8cm, right=1.8cm, top=1.3cm, bottom=1.8cm]{{geometry}}
\usepackage{{booktabs}}
\usepackage{{tabularx}}
\usepackage{{array}}
\usepackage{{enumitem}}
\usepackage{{titlesec}}
\usepackage{{fancyhdr}}
\usepackage{{fontenc}}
\usepackage{{inputenc}}
\usepackage{{microtype}}
\usepackage{{parskip}}
\usepackage{{hyperref}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}

\hypersetup{{hidelinks, colorlinks=false}}

%% ── Table helpers ─────────────────────────────────────────
\newcolumntype{{L}}[1]{{>{{\raggedright\arraybackslash}}p{{#1}}}}

%% ── Section headings ──────────────────────────────────────
\titleformat{{\section}}{{\large\bfseries}}{{}}{{0em}}{{}}[\titlerule]
\titleformat{{\subsection}}{{\normalsize\bfseries}}{{}}{{0em}}{{}}
\titleformat{{\subsubsection}}{{\normalsize\bfseries}}{{}}{{0em}}{{}}

\titlespacing{{\section}}{{0pt}}{{12pt}}{{4pt}}
\titlespacing{{\subsection}}{{0pt}}{{8pt}}{{3pt}}
\titlespacing{{\subsubsection}}{{0pt}}{{6pt}}{{2pt}}

%% ── Page style ────────────────────────────────────────────
\pagestyle{{fancy}}
\fancyhf{{}}
\renewcommand{{\headrulewidth}}{{0pt}}
\fancyfoot[C]{{\small Cognitive Psychology --- Week {week_num} \textbar\ Page \thepage}}

%% ── Misc helpers ──────────────────────────────────────────
\newcommand{{\bb}}[1]{{\textbf{{#1}}}}
\setlength{{\parskip}}{{4pt}}

%% ═══════════════════════════════════════════════════════════
\begin{{document}}
\setlength{{\arrayrulewidth}}{{0.4pt}}

\begin{{center}}
\bfseries\LARGE Introduction to Cognitive Psychology\par
\vspace{{0.2cm}}
\large Assignment {week_num} Detailed Solutions
\end{{center}}
\vspace{{0.5cm}}

%% ════════════════════════════════════════════════════════════
\section*{{ASSIGNMENT {week_num} --- Full Solutions with Explanations}}
"""

def clean_target(text):
    text = text.replace("✅", "")
    text = text.replace("**", "").strip()
    return text

def parse_markdown(file_path, week_num):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by questions
    parts = re.split(r'### Question (\d+)', content)
    
    latex_out = template.format(week_num=week_num)

    # Process all questions
    for i in range(1, len(parts), 2):
        q_num = parts[i]
        q_block = parts[i+1]
        
        # We might have div closing, hr, etc
        q_block = q_block.split('Summary Table')[0]
        
        # Find question text
        q_text_match = re.search(r'\*\*(.+?)\*\*(?=\n\n\s*[-*])', q_block, re.DOTALL)
        if not q_text_match:
            q_text_match = re.search(r'\*\*(.+?)\*\*(?=\n(?:-|\*))', q_block, re.DOTALL)
        
        q_text = q_text_match.group(1).replace('\n', ' ').strip()
        # Fix escaping
        q_text = q_text.replace("\\_", "_") # remove preexisting escapes
        q_text = q_text.replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")
        
        latex_out += f"\n\\subsubsection*{{Question {q_num}}}\n"
        latex_out += f"\\textit{{{q_text}}}\n\\medskip\n\n\\begin{{tabular}}{{L{{0.3cm}} L{{14.9cm}}}}\n"
        
        # Find options - robust matching 
        options = re.findall(r'[-*]\s*(?:\*\*)?(A|B|C|D)\.\s+(.*?)(?:\*\*)?(?=\n|$)', q_block)
        for opt_letter, opt_content in options:
            opt_clean = clean_target(opt_content).replace("\\_", "_").replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")
            if "✅" in opt_content or "Correct" in opt_content:
                latex_out += f"& \\textbf{{{opt_letter}.\\ {opt_clean} \\checkmark}} \\\\\n"
            else:
                latex_out += f"& {opt_letter}.\\ {opt_clean} \\\\\n"
                
        latex_out += "\\end{tabular}\n\n\\vspace{0.3cm}\n"
        
        # Find answer and explanation
        ans_match = re.search(r'\*\*Answer:\s*(.+?)\*\*', q_block)
        ans_text = clean_target(ans_match.group(1)) if ans_match else ""
        ans_text = ans_text.replace("\\_", "_").replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")
        
        latex_out += f"\\noindent\\textbf{{Ans:}} {ans_text}\\\\[0.2cm]\n"
        
        exp_match = re.search(r'\*\*Explanation:\*\*\s*(.+?)(?=\n\n(?:_|<|>|-))', q_block, re.DOTALL)
        if exp_match:
            exp_text = exp_match.group(1).strip()
            # Basic fixes for latex bold/italic
            exp_text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', exp_text)
            exp_text = re.sub(r'_(.+?)_', r'\\textit{\1}', exp_text)
            exp_text = exp_text.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#")
            latex_out += f"\\textbf{{Why this answer:}} \\\\\n{exp_text}\n\\vspace{{0.4cm}}\n"
            
        if int(q_num) == 6 or int(q_num) == 3 and week_num == 4:
            latex_out += "\\newpage\n"

    # Extract summary table
    table_match = re.search(r'## Summary Table\n\n(.+?)(?=\n\n---|_Ref)', content, re.DOTALL)
    latex_out += "\n\\medskip\n\\subsection*{Assignment Quick Answer Summary}\n\n\\begin{center}\n\\renewcommand{\\arraystretch}{1.4}\n\\begin{tabular}{|L{0.8cm}|L{6.2cm}|L{8.2cm}|}\n\\hline\n\\bb{Q\\#} & \\bb{Topic} & \\bb{Correct Answer} \\\\\n\\hline\n"
    
    if table_match:
        table_lines = table_match.group(1).strip().split('\n')
        for line in table_lines[2:]:
            if not line.strip() or "---" in line: continue
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if len(cells) >= 3:
                latex_out += f"{cells[0]} & {cells[1].replace('&', '\\&').replace('_', '\\_')} & {cells[2].replace('&', '\\&').replace('_', '\\_')} \\\\\n"
    
    latex_out += "\\hline\n\\end{tabular}\n\\end{center}\n\n\\medskip\n"
    
    ref_match = re.search(r'_(Ref:.+?)_', content)
    if ref_match:
        ref_text = ref_match.group(1).replace("&", "\\&").replace("_", "\\_")
        latex_out += f"{{\\small\\textit{{{ref_text}}}}}\n\n\\end{{document}}\n"
    else:
        latex_out += "\\end{document}\n"

    out_file = f"/Users/ankitkumar/Downloads/NPTEL_sem_8/Introduction To Cognitive Psychology/latex-code-for-cognitive-Psychol/CognitivePsychology_Week{week_num}.tex"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(latex_out)
    print(f"Generated {out_file}")

for w in range(2, 8):
    p = f"/Users/ankitkumar/Downloads/NPTEL_sem_8/Introduction To Cognitive Psychology/week_{w}.md"
    if os.path.exists(p):
        parse_markdown(p, w)
