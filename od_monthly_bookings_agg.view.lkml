view: od_monthly_bookings_agg  {
  sql_table_name: `MIDT_CONSUMPTION.OD_MONTHLY_BOOKINGS_AGG` ;;

  dimension: GDS_ID {
    type: string
    primary_key: yes
    sql: ${TABLE}.GDS_ID ;;
    hidden: no
  }

  dimension: Departure_Date_key {
    type: date
    primary_key: no
    sql: ${TABLE}.DEPARTURE_DATE ;;
    hidden: no
  }

  dimension: Passenger_Count {
    type: number
    primary_key: no
    sql: ${TABLE}.PASSENGER_COUNT ;;
    hidden: no
  }
}

