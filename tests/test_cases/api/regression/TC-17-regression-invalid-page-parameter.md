### TC-17: Некорректные параметры пагинации

**Тип:** Регрессионный
**Приоритет:** Средний
**Предусловия:** Backend запущен

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog?page=0 | HTTP 400, `statusCode=400`, `error="BAD_REQUEST"` (page min = 1) |
| 2 | GET /api/v1/catalog?page=-1 | HTTP 400, `statusCode=400`, `error="BAD_REQUEST"` |
| 3 | GET /api/v1/catalog?pageSize=0 | HTTP 400, `statusCode=400`, `error="BAD_REQUEST"` (pageSize min = 1) |
| 4 | GET /api/v1/catalog?pageSize=101 | HTTP 400, `statusCode=400`, `error="BAD_REQUEST"` (pageSize max = 100) |

**Постусловия:** Нет
