# masterdoc-lite

Лендинг **lite.masterdoc.pro** (статика в `landing/`).

## Локальный просмотр

```bash
cd landing && python3 -m http.server 8765
```

http://localhost:8765/

## Деплой

Push в `main` → GitHub Actions rsync на `91.207.75.72`, nginx `lite.masterdoc.pro`.

Перед первым деплоем:

1. DNS: `lite.masterdoc.pro` → `91.207.75.72`
2. На сервере: `nginx`, `certbot` (как на api VPS)
3. Секреты в репозитории (см. ниже)

## Секреты GitHub (`Settings` → `Secrets and variables` → `Actions`)

| Секрет | Обязательный | Описание |
|--------|--------------|----------|
| `DEPLOY_SSH_PRIVATE_KEY` | да | Приватный ключ SSH (ed25519), публичная часть в `~/.ssh/authorized_keys` на сервере |
| `DEPLOY_USER` | да | Пользователь SSH, например `root` или `deploy` |
| `CERTBOT_EMAIL` | нет | Email для Let's Encrypt; по умолчанию `admin@masterdoc.pro` |

Хост и пути зашиты в workflow: `91.207.75.72`, сайт `/var/www/lite.masterdoc.pro`, конфиги `/opt/masterdoc-lite`.

## Структура

- `landing/` — HTML/CSS/JS лендинга
- `deploy/` — nginx и скрипт установки
- `.github/workflows/ci.yml` — CI и деплой
