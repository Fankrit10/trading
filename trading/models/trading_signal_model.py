"""
Model for Trading Signal Processing
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TradingSignal(BaseModel):
    """
    Trading signal structure
    """
    datetime: datetime
    close: float
    signal: int


class TradingPerformance(BaseModel):
    """
    Trading performance structure
    """
    cumulative_return: float = 0.0
    last_close: Optional[float] = None
    position: int = 0
    timestamp: datetime = Field(default_factory=datetime.utcnow)
