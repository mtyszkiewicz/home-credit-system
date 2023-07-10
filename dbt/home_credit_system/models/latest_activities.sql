WITH max_dates AS (
    SELECT 
        icon, 
        MAX(start_date) AS latest_start_date
    FROM {{ source('raw', 'activities') }}
    GROUP BY icon
)

SELECT 
    a.id,
    a.name,
    m.icon,
    a.value,
    a.start_date,
    a.end_date
FROM {{ source('raw', 'activities') }} a
JOIN max_dates m ON a.icon = m.icon AND a.start_date = m.latest_start_date
