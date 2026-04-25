### TC-6: Просмотр каталога — от списка к карточке товара с локализацией

**Тип:** E2E
**Приоритет:** Критический
**Предусловия:** Backend запущен, каталог синхронизирован

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog?lang=ru | HTTP 200, `language="ru"`, `items` — массив с товарами, `meta.sourceLanguage="en"` |
| 2 | Извлечь первый товар | `items[0]` содержит `id`, `title` (на русском), `price`, `category` |
| 3 | GET /api/v1/catalog/{items[0].id}?lang=ru | HTTP 200, `language="ru"`, `product.id` совпадает с запрошенным, `product.title` совпадает с `items[0].title` из шага 1 |
| 4 | Проверить данные карточки | `product.category.slug` совпадает с `items[0].category.slug` из шага 1 |

**Постусловия:** Нет
