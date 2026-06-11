from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

console = Console()

def show_dashboard(owner, model):

    console.clear()

    console.print("""
███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
""", style="bold cyan")

    left = Panel(
f"""
Owner      : {owner}
Model      : {model}

AI Core    : Online
Memory     : Active
Ollama     : Connected
Agents     : Ready
""",
title="SYSTEM"
    )

    right = Panel(
"""
/chat
/code
/model
/help
/exit
""",
title="COMMANDS"
    )

    console.print(Columns([left, right]))
    console.print("\n[bold green]◉ Cognitive Matrix Online[/bold green]")