set fish_greeting
# Alias for ls/lsd
#alias ls='lsd'  # commented out because it was missing some directories
#alias la='lsd -a'

set PATH /home/rjslater/anaconda3/bin $PATH
set PATH /usr/lc3/ $PATH

# SSH Aliases
alias jarvis='/home/rjslater/sshJARVIS.py'
alias kowalski='/home/rjslater/sshJulien.py'
alias julien='/home/rjslater/sshJulien.py'

# IP Scanner
alias ipscan='sudo nmap -sS -p 22 192.168.1.0/24'

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval (eval /home/rjslater/anaconda3/bin/conda "shell.fish" "hook" $argv)
# <<< conda initialize <<<

# Quick ping check alias
alias ping="ping 8.8.8.8 -c 5"

# Ree for those ree moments
alias ree="yes rEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

# For when you're upset and using sudo
alias fucking="sudo"
