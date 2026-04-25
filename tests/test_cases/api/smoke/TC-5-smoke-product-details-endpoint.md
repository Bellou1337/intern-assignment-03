### TC-5: Получение карточки товара по ID

**Тип:** Smoke
**Приоритет:** Критический
**Предусловия:** Backend запущен, каталог синхронизирован

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog | HTTP 200, извлечь `items[0].id` как `productId` |
| 2 | GET /api/v1/catalog/{productId} | HTTP 200, ответ содержит поля `language`, `currency`, `product`, `reviews`, `meta` |
| 3 | Проверить структуру product | `product.id` совпадает с `productId`, содержит поля `title`, `description`, `price`, `rating`, `imageUrl`, `category` |
| 4 | Проверить reviews | `reviews` — массив (может быть пустым), каждый элемент содержит `id`, `rating`, `comment`, `date`, `reviewerName` |

**Постусловия:** Нет
