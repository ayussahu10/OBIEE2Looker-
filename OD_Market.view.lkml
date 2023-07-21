view: OD_Market  {
  sql_table_name: `MIDT_CONSUMPTION.CLIENT_AIRPORT_PAIR_DIM` ;;

  dimension: AIRPP_ID {
    type: string
    primary_key: yes
    sql: ${TABLE}.AIRPP_ID ;;
    hidden: no
  }

  dimension: CLIENT_ID {
    type: string
    primary_key: no
    sql: ${TABLE}.CLIENT_ID ;;
    hidden: no
  }

  dimension: Origin_Airport_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.AIRPP_DEPART_AIRP_CODE ;;
    hidden: no
  }

  dimension: Origin_City_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.CTY_DEP_CITY_CODE ;;
    hidden: no
  }

  dimension: Origin_Country_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.CO_DEP_CNTRY_CODE ;;
    hidden: no
  }

  dimension: Origin_Region_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.WA_DEP_WA_CODE ;;
    hidden: no
  }
}
```