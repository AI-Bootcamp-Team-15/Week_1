from BaseChefGPT import BaseChefGPT
from shared import common_prompt

class ArcheksChef(BaseChefGPT):
  def __init__(self):
    BaseChefGPT.__init__(self)

    self.name = "Archeks"
    self.messages = [{
      "role": "system",
      "content": f'You are an experienced old spirited Georgian cook that assists people with cooking-related tasks.\n{common_prompt}'
    }]
