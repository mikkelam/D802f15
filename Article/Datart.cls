\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{datart}[2014/11/30]

% OPTIONS
\RequirePackage{kvoptions}
  \SetupKeyvalOptions{%
    family=ML,
    prefix=ML@,
  }

\DeclareStringOption[english]{language}
\DeclareStringOption[11pt]{fontsize}
\DeclareStringOption[twocolumn]{columns}
\DeclareStringOption[LightGrey]{boxcolor}
\DeclareStringOption[LightGrey]{examplecolor}
\DeclareStringOption[true]{cleveref}
\DeclareStringOption[utf8]{inputenc}
\DeclareStringOption[T1]{fontenc}
\DeclareStringOption[true]{lmodern}
\DeclareStringOption[true]{indentfirst}
\DeclareStringOption[]{microtype}
\DeclareStringOption[section]{placeins}
\DeclareStringOption[authoryear]{natbib}
\ProcessKeyvalOptions*

% BABEL, INPUTENC ETC...
\PassOptionsToPackage{\ML@language}{babel}
\PassOptionsToPackage{\ML@inputenc}{inputenc}
\PassOptionsToPackage{\ML@fontenc}{fontenc}
\PassOptionsToPackage{\ML@microtype}{microtype}
\PassOptionsToPackage{\ML@placeins}{placeins}
\PassOptionsToPackage{\ML@natbib}{natbib}

\PassOptionsToClass{\ML@fontsize,\ML@columns}{article}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessOptions\relax

\LoadClass{article}
\RequirePackage{babel}
\RequirePackage{inputenc}
\RequirePackage{fontenc}
\RequirePackage{microtype}
\RequirePackage[top=1in,bottom=1in,left=1.2in,right=1.2in]{geometry}

% CUSTOM SECTION HEADINGS
\RequirePackage{titlesec}
\newcommand{\hsp}{\hspace{20pt}}
\titleformat{\section}
  {\Large\scshape\raggedright}
  {\thesection\hsp}{0pt}
  {}
  [\titlerule]

\titleformat{\subsection}
  {\large\scshape\raggedright}
  {\thesubsection\hsp}{0pt}
  {}
  [\titlerule]

% PACKAGES FOR THEOREMS, DEFINITIONS ETC.
\RequirePackage{colortbl}
\RequirePackage[dvipsnames,svgnames]{xcolor}
\RequirePackage{amsthm}
\RequirePackage{adjustbox}

% COLOR BOX
\makeatletter
\newenvironment{amsthmbox}{%
    \noindent
    \adjustbox{innerenv={varwidth}[l]{0.9\linewidth},margin=\fboxsep+.25cm \fboxsep+.2cm,bgcolor={\ML@boxcolor},frame,center}
}{%
    \relax
}
\makeatother

% EXAMPLE COLOR BOX
\makeatletter
\newenvironment{examsthmbox}{%
    \noindent
    \adjustbox{innerenv={varwidth}[l]{0.9\linewidth},margin=\fboxsep+.25cm \fboxsep+.2cm,bgcolor={\ML@examplecolor},frame,center}
}{%
    \relax
}
\makeatother

% PACKAGES
% AMS
\RequirePackage{amsmath, amsfonts, amssymb}

% New floats and captions
\RequirePackage{newfloat}
\RequirePackage{caption}

% Tables
\RequirePackage{longtable} %Enable tables to span multiple sides
\RequirePackage{multirow} %Enable multirows in tables

% Layout
\RequirePackage{setspace}

% Better author/department
\RequirePackage[affil-it]{authblk}

% Manipulating graphics and more
\RequirePackage{scalefnt} %Enable scaling of fonts
\RequirePackage{rotating} %Enable rotating

% Graphics
\RequirePackage{graphicx} %JPG, PNG etc.
\RequirePackage{tikz} %Vector graphics
\RequirePackage{pgfplotstable} 
\RequirePackage{subcaption}
\RequirePackage{placeins} %Floatdump etc.
\RequirePackage{pdfpages} %PDF pages

% Code
\RequirePackage{listings} %Enable environment for code

% Algorithms / pseudo code
\RequirePackage{clrscode}

% EPS support
\RequirePackage{epstopdf}

% Bibliography
\RequirePackage{natbib}
\bibliographystyle{apalike}

% REFERENCES
\RequirePackage[bookmarks=true,bookmarksopen=true,bookmarksnumbered=true,colorlinks=true,breaklinks=true,backref=page,linkcolor=blue,citecolor=blue]{hyperref}
\RequirePackage{url}
\RequirePackage{etoolbox}

\makeatletter
\expandafter\ifstrequal\expandafter{\ML@cleveref}{true}{%
  \RequirePackage[\ML@language]{cleveref}
}
{%
  \relax}
\makeatother

% LMODERN OR NOT?
\makeatletter
\expandafter\ifstrequal\expandafter{\ML@lmodern}{true}{%
  \RequirePackage{lmodern}
}
{%
  \relax}
\makeatother

% DEFINITION
\makeatletter
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{tempDef}{Definition}[section]
\newenvironment{boxdefinition}{%
  \vspace{2mm}
  \noindent
  \amsthmbox\bgroup\tempDef
}{%
  \egroup\vspace{2mm}
}
\makeatother

% THEOREM
\makeatletter
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{tempTheo}{Theorem}[section]
\newenvironment{boxtheorem}{%
  \vspace{2mm}
  \noindent
  \amsthmbox\bgroup\tempTheo
}{%
  \egroup\vspace{2mm}
}
\makeatother

% PROPOSITION
\makeatletter
\theoremstyle{plain}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{tempProp}{Proposition}[section]
\newenvironment{boxproposition}{%
  \vspace{2mm}
  \noindent
  \amsthmbox\bgroup\tempProp
}{%
  \egroup\vspace{2mm}
}
\makeatother

% LEMMA
\makeatletter
\theoremstyle{plain}
\newtheorem{lemma}{Lemma}[section]
\newtheorem{tempLem}{Lemma}[section]
\newenvironment{boxlemma}{%
  \vspace{2mm}
  \noindent
  \amsthmbox\bgroup\tempLem
}{%
  \egroup\vspace{2mm}
}
\makeatother

% COROLLARY
\makeatletter
\theoremstyle{plain}
\newtheorem{corollary}{Corollary}[section]
\newtheorem{tempCoro}{Corollary}[section]
\newenvironment{boxcorollary}{%
  \noindent
  \amsthmbox\bgroup\tempCoro
}{%
  \egroup\vspace{2mm}
}
\makeatother

% FACT
\makeatletter
\theoremstyle{plain}
\newtheorem{fact}{Fact}[section]
\newtheorem{tempFact}{Fact}[section]
\newenvironment{boxfact}{%
  \vspace{2mm}
  \noindent
  \amsthmbox\bgroup\tempFact
}{%
  \egroup\vspace{2mm}
}
\makeatother

% PROOF
\makeatletter
\theoremstyle{definition}
\newtheorem{tempProof}{Proof}[section]
\newenvironment{boxproof}{%
  \vspace{2mm}
  \noindent
  \amsthmbox\bgroup\tempProof
}{%
  $\qed$\egroup\vspace{2mm}
}
\makeatother

% EXAMPLE
\makeatletter
\theoremstyle{plain}
\newtheorem{example}{Example}[section]
\newtheorem{tempEx}{Example}[section]
\newenvironment{boxexample}{%
  \vspace{2mm}
  \noindent
  \examsthmbox\bgroup\tempEx
}{%
  \egroup\vspace{2mm}
}
\makeatother

