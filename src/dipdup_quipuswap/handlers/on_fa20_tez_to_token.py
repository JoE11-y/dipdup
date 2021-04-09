from dipdup.models import HandlerContext, OperationContext
from dipdup_quipuswap.models import *
from dipdup_quipuswap.types.KT1CiSKXR68qYSxnbzjwvfeMCRburaSDonT2.parameter.tezToTokenPayment import Teztotokenpayment
from dipdup_quipuswap.types.KT1K9gCRgaLRFKTErYt1wVxA3Frb9FjasjTV.parameter.transfer import Transfer


async def on_fa20_tez_to_token(
    ctx: HandlerContext,
    tezToTokenPayment: OperationContext[Teztotokenpayment],
    transfer: OperationContext[Transfer],
) -> None:
    ...