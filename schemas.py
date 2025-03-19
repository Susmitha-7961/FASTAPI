from pydantic import BaseModel
from typing import List, Optional

class Dependency(BaseModel):
  id: int
  name: str
  version: str
  vulnerabilities: Optional[List[str]]=[]

class Application(BaseModel):
  id: int
  name: str
  description: str
  dependencies: List[Dependency]=[]
  
