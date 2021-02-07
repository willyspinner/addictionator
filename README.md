# Useful links
- [riot games developer portal](https://developer.riotgames.com/)
- [email client](https://sendgrid.com/)
- [email client 2](https://www.mailgun.com/)


## Riot developer portal API Instructions

1. Lookup `encryptedSummonerId` by summoner name [here](https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName) (`GET /lol/summoner/v4/summoners/by-name/{summonerName}`)
2. Using the `encryptedSummonerId`, lookup any active matches [here](https://developer.riotgames.com/apis#spectator-v4/GET_getCurrentGameInfoBySummoner) (`GET /lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}`)

