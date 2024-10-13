from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World


class SOHWeb(WebWorld):
  setup = Tutorial(
      "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Ship of Harkinian software on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["puzzler995"]
  )

  tutorials = [setup]

class SOHWorld(World):
  """
  It's OOT but better
  """

game: str = "Ship of Harkinian"
