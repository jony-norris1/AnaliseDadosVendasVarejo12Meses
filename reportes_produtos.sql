-- Query para identificar os produtos mais vendidos
SELECT car_model, COUNT(*) as total_sales
FROM base
GROUP BY car_model
ORDER BY total_sales DESC
LIMIT 5;

-- Query para identificar os dias da semana com mais vendas
SELECT DATE_FORMAT(date, '%W') as day_of_week, COUNT(*) as total_sales
FROM base
GROUP BY day_of_week
ORDER BY total_sales DESC;

-- Query para identificar as regiões com mais vendas
SELECT manufacturer, COUNT(*) as total_sales
FROM base
GROUP BY manufacturer
ORDER BY total_sales DESC;
