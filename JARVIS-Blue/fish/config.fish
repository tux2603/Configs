set fish_greeting
# Alias for ls/lsd
#alias ls='lsd'  # commented out because it was missing some directories
#alias la='lsd -a'

set PATH /home/rjslater/anaconda3/bin $PATH
set PATH /usr/lc3 $PATH

# SSH Aliases
alias friday='/home/rjslater/sshFRIDAY.py'
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

# Backup alias
alias backup="/home/rjslater/backupJarvis.sh ; /home/rjslater/backupJulien.sh"
