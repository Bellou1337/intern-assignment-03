### TC-4: Получение каталога товаров (дефолтные параметры)

**Тип:** Smoke
**Приоритет:** Критический
**Предусловия:** Backend запущен, каталог синхронизирован с DummyJSON

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog | HTTP 200, ответ содержит поля `language`, `currency`, `categories`, `items`, `meta` |
| 2 | Проверить дефолтные значения | `language="en"`, `currency="USD"`, `meta.currentPage=1`, `meta.pageSize=20`, `meta.sort="price_asc"` |
| 3 | Проверить структуру items | `items` — массив, каждый элемент содержит поля `id`, `title`, `description`, `price` (объект с `amount` и `currency`), `rating`, `imageUrl`, `category` (объект с `slug` и `title`) |
| 4 | Проверить категории | `categories` — массив объектов с полями `slug` и `title`, количество `>= 1` |
| 5 | Проверить мета-данные | `meta.totalProducts >= 1`, `meta.totalPages >= 1`, `meta.sourceLanguage="en"`, `meta.sourceCurrency="USD"` |

**Постусловия:** Нет
