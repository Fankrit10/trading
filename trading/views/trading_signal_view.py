"""
Views for Trading Signal Processing
"""
# pylint: disable=W0718
from fastapi import APIRouter
from trading.controllers.trading_signal_controller import (process_signal,
                                                           get_performance, get_history,
                                                           enhance_trading_performance)
from trading.models.trading_signal_model import TradingSignal

router = APIRouter()


@router.post("/signal", tags=["trading"])
async def post_signal(signal: TradingSignal):
    """
    Post a trading signal for processing
    """
    return await process_signal(signal)


@router.get("/performance", tags=["trading"])
async def get_current_performance():
    """
    Get the current portfolio cumulative return
    """
    return await get_performance()


@router.get("/enhance_performance", tags=["trading"])
async def get_trading_enhancement():
    """
    Endpoint to enhance trading performance based on history using LLM
    """
    return await enhance_trading_performance()


@router.get("/history", tags=["trading"])
async def get_signal_history():
    """
    Get full history of processed trading signals
    """
    return await get_history()
