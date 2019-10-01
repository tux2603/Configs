set fish_greeting

set PATH /home/rjslater/anaconda3/bin $PATH

# SSH Aliases
alias friday='/home/rjslater/sshFRIDAY.py'
alias kowalski='/home/rjslater/sshJulien.py'
alias julien='/home/rjslater/sshJulien.py'

# IP Scanner
alias ipscan='sudo nmap -sS -p 22 192.168.1.0/24'

# Quick ping check alias
alias ping="ping 8.8.8.8 -c 5"

# Backup alias
alias backup="/home/rjslater/backupJarvis.sh ; /home/rjslater/backupToJulien.sh"

# lsd instead of ls
alias ls="lsd"
alias la="lsd -al"

# Start X on login
if status --is-login
    if test -z "$DISPLAY" -a $XDG_VTNR = 1
        exec startx
    end
end

# Pfetch is a lighter neofetch
sh pfetch
