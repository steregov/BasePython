"""
create dataclass `Engine`
"""
@dataclass
#(init=True) -- делать или не делать инит
class Engine:
    volume: int
    pistons: int

