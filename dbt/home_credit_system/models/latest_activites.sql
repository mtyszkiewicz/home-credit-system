WITH max_dates AS (
    SELECT 
        icon AS activity_code, 
        MAX(start_date) AS latest_start_date
    FROM {{ source('raw', 'activities') }}
    GROUP BY icon
)

SELECT 
    a.id,
    a.name,
    m.activity_code,
    a.value,
    m.latest_start_date,
    a.end_date
FROM {{ source('raw', 'activities') }} a
JOIN max_dates m ON a.icon = m.activity_code AND a.start_date = m.latest_start_date
