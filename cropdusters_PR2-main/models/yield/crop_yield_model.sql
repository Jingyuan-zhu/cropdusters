
-- Use the `ref` function to select from other models

    SELECT 
        Symbol
    FROM 
         {{ source('cropdusters', 'crop_yield') }}