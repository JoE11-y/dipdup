import logging
from typing import Any, Dict, List, Optional

from dipdup.config import HTTPConfig
from dipdup.http import HTTPGateway

TOKENS_REQUEST_LIMIT = 10


class BcdDatasource(HTTPGateway):
    def __init__(
        self,
        url: str,
        network: str,
        http_config: Optional[HTTPConfig] = None,
    ) -> None:
        super().__init__(url, http_config)
        self._logger = logging.getLogger('dipdup.bcd')
        self._network = network

    async def run(self) -> None:
        pass

    async def resync(self) -> None:
        pass

    async def get_tokens(self, address: str) -> List[Dict[str, Any]]:
        tokens, offset = [], 0
        while True:
            tokens_batch = await self._http.request(
                'get',
                url=f'v1/contract/{self._network}/{address}/tokens?offset={offset}',
            )
            tokens += tokens_batch
            offset += TOKENS_REQUEST_LIMIT
            if len(tokens_batch) < TOKENS_REQUEST_LIMIT:
                break
        return tokens

    async def get_token(self, address: str, token_id: int) -> Dict[str, Any]:
        return await self._http.request(
            'get',
            url=f'v1/contract/{self._network}/{address}/tokens?token_id={token_id}',
        )

    def _default_http_config(self) -> HTTPConfig:
        return HTTPConfig(
            cache=True,
            retry_count=3,
            retry_sleep=1,
            ratelimit_rate=100,
            ratelimit_period=30,
        )