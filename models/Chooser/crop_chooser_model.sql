
    SELECT 
        *
    FROM 
       {{ source('cropdusters', 'crop_weather') }}
