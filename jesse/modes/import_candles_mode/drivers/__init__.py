from pydoc import locate
from jesse.enums import exchanges
from jesse.modes.import_candles_mode.drivers.BinanceSpot import BinanceSpot
from jesse.modes.import_candles_mode.drivers.BinanceUSSpot import BinanceUSSpot
from jesse.modes.import_candles_mode.drivers.BinancePerpetualFutures import BinancePerpetualFutures
from jesse.modes.import_candles_mode.drivers.BitfinexSpot import BitfinexSpot
from jesse.modes.import_candles_mode.drivers.CoinbaseSpot import CoinbaseSpot
from jesse.modes.import_candles_mode.drivers.BinancePerpetualFuturesTestnet import BinancePerpetualFuturesTestnet
from jesse.modes.import_candles_mode.drivers.BybitUSDTPerpetual import BybitUSDTPerpetual
from jesse.modes.import_candles_mode.drivers.BybitUSDTPerpetualTestnet import BybitUSDTPerpetualTestnet
from jesse.modes.import_candles_mode.drivers.FTXPerpetualFutures import FTXPerpetualFutures
from jesse.modes.import_candles_mode.drivers.FTXSpot import FTXSpot
from jesse.modes.import_candles_mode.drivers.FTXUSSpot import FTXUSSpot


_builtin_drivers = {
    # Perpetual Futures
    exchanges.BINANCE_PERPETUAL_FUTURES: BinancePerpetualFutures,
    exchanges.BINANCE_PERPETUAL_FUTURES_TESTNET: BinancePerpetualFuturesTestnet,
    exchanges.BITFINEX_SPOT: BitfinexSpot,
    exchanges.COINBASE_SPOT: CoinbaseSpot,
    exchanges.BYBIT_USDT_PERPETUAL: BybitUSDTPerpetual,
    exchanges.BYBIT_USDT_PERPETUAL_TESTNET: BybitUSDTPerpetualTestnet,
    exchanges.FTX_PERPETUAL_FUTURES: FTXPerpetualFutures,

    # Spot
    exchanges.FTX_SPOT: FTXSpot,
    exchanges.FTX_US_SPOT: FTXUSSpot,
    exchanges.BINANCE_SPOT: BinanceSpot,
    exchanges.BINANCE_US_SPOT: BinanceUSSpot
}

_local_drivers = locate('plugins.import_candles_drivers')

# drivers must be a dict which is merged of _builtin_drivers and _local_drivers
drivers = {}
drivers.update(_builtin_drivers)
if _local_drivers is not None:
    drivers.update(_local_drivers)
