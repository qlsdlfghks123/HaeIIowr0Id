import yaml
from auth_ut import get_access_token, revoke_token

with open(r"C:\Users\qlsdl\KIS\config\kis_devlp.yaml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

token = get_access_token(config)
print(f"발급 받은 토큰: {token}")


if token:
    result = revoke_token(config, token)
    print(f"폐기 결과: {result}")
