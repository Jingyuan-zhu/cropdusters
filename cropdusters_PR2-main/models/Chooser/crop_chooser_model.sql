
    SELECT 
        state_alpha,
    FROM 
       {{ source('cropdusters', 'crop_chooser') }}
