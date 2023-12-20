/* Agg average crop price, merge on same year and same crop, find profit for region's yield */
WITH aggregated_prices AS (
    SELECT
        Symbol,
        AVG(close) AS mean_close,
        date,
        EXTRACT(YEAR FROM date) AS year
    FROM {{ source('cropdusters', 'crop_price') }}
    GROUP BY Symbol, date
),
joined_data AS (
    SELECT
        ap.date,
        ap.Symbol,
        ap.mean_close,
        cy.Value,
        cy.commodity_desc,
        cy.state_alpha,
        cy.year,
        cy.Value * cy.state_alpha AS revenue  -- Calculate area's revenue
    FROM aggregated_prices ap
    JOIN {{ source('cropdusters', 'crop_yield') }} cy
    ON ap.Symbol = UPPER(cy.commodity_desc) AND EXTRACT(YEAR FROM ap.date) = cy.year
)
SELECT * FROM joined_data;
