"""
Description:    dataclasses for GPS messages to print to screen
Creation Date:  07/04/22
"""
from dataclasses import dataclass

@dataclass
class AbstractMessage:
    pass

@dataclass
class GPSLocationMessage(AbstractMessage):
    pass

@dataclass
class LockInProgressMessage(AbstractMessage):
    pass

@dataclass
class StartUpMessage(AbstractMessage):
    pass

@dataclass
class ShutDownMessage(AbstractMessage):
    pass
