view: OD_GDS  {
  sql_table_name: `MIDT_CONSUMPTION.GDS_DIM` ;;

  dimension: GDS_ID {
    type: string
    primary_key: yes
    sql: ${TABLE}.GDS_ID ;;
    hidden: yes
  }

  dimension: GDS_TYPE_CODE {
    type: string
    primary_key: no
    sql: ${TABLE}.GDS_TYPE_CODE ;;
    hidden: no
  }

  dimension: GDS_Name {
    type: string
    primary_key: no
    sql: ${TABLE}.GDS_NAME ;;
    hidden: no
  }

  dimension: GDS_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.GDS_CODE ;;
    hidden: no
  }
}

