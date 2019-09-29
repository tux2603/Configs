set fish_greeting

set PATH /home/rjslater/anaconda3/bin $PATH

# SSH Aliases
alias kowalski='/home/rjslater/sshJulien.py'
alias julien='/home/rjslater/sshJulien.py'

# IP Scanner
alias ipscan='sudo nmap -sS -p 22 192.168.1.0./24'

# Backup alias
alias backup='/home/rjslater/backupFRIDAY.sh ; /home/rjslater/backupToJulien.sh'

# Conda init
eval (eval /home/rjslater/anaconda3/bin/conda "shell.fish" "hook" $argv)

# Quick ping alias check
alias ping="ping 8.8.8.8 -c 5"

# lsd instead of ls
alias ls="lsd"
alias la="lsd -al"

# Start X on login
if status --is-login
    if test -z "$DISPLAY" -a $XDG_VTNR = 1
        exec startx
    end
end
