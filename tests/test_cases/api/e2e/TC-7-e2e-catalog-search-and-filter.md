### TC-7: Поиск товара по названию и фильтрация по категории

**Тип:** E2E
**Приоритет:** Средний
**Предусловия:** Backend запущен, каталог синхронизирован

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog | HTTP 200, извлечь `categories[0].slug` и первый `items[0].title` (или его часть) |
| 2 | GET /api/v1/catalog?query={часть title} | HTTP 200, `meta.query` содержит переданный query, все `items[i].title` или `items[i].description` содержат поисковый запрос (case-insensitive) |
| 3 | GET /api/v1/catalog?category={slug} | HTTP 200, `meta.category` = переданный slug, все `items[i].category.slug` совпадают с переданным |
| 4 | GET /api/v1/catalog?query={часть title}&category={slug} | HTTP 200, результаты удовлетворяют обоим условиям: поисковый запрос + категория |

**Постусловия:** Нет
