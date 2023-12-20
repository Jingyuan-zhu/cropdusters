
-- Use the `ref` function to select from other models

    SELECT 
        *
    FROM 
         {{ source('cropdusters', 'crop_yield') }}