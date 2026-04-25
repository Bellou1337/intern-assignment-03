### TC-20: Карточка товара — локализация и конвертация вместе

**Тип:** Регрессионный
**Приоритет:** Средний
**Предусловия:** Backend запущен, каталог синхронизирован, курсы загружены

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog | HTTP 200, извлечь `items[0].id` |
| 2 | GET /api/v1/catalog/{id}?lang=de&currency=EUR | HTTP 200, `language="de"`, `currency="EUR"`, `product.price.currency="EUR"`, `product.title` — переведённый (не пустой) |
| 3 | GET /api/v1/catalog/{id}?lang=en&currency=USD | HTTP 200, `language="en"`, `currency="USD"`, `product.price.currency="USD"` |
| 4 | Сравнить цены | Цена в EUR отличается от цены в USD (если курс != 1) |

**Постусловия:** Нет
