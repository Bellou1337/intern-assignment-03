### TC-8: Пагинация каталога — последовательный перебор страниц

**Тип:** E2E
**Приоритет:** Средний
**Предусловия:** Backend запущен, каталог содержит > 20 товаров

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog?pageSize=5 | HTTP 200, `items` содержит <= 5 элементов, `meta.currentPage=1`, `meta.pageSize=5`, `meta.totalProducts > 5`, `meta.totalPages > 1` |
| 2 | GET /api/v1/catalog?pageSize=5&page=2 | HTTP 200, `meta.currentPage=2`, `items` содержит <= 5 элементов, `items[0].id` отличается от `items[0].id` шага 1 |
| 3 | GET /api/v1/catalog?pageSize=5&page={totalPages} | HTTP 200, `meta.currentPage=totalPages`, `items` может содержать < 5 элементов |
| 4 | GET /api/v1/catalog?pageSize=5&page={totalPages+1} | HTTP 200, `items` — пустой массив, `meta.currentPage=totalPages+1` |

**Постусловия:** Нет
