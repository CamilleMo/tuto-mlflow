curl http://824396ba-fc31-4c16-ac57-1228e7fae53d.westeurope.azurecontainer.io/score -H 'Content-Type: application/json; format=pandas-split' -d '{"columns":["B1", "B2", "B3"], "data":[[1, 2, 3]]}'
echo ""

curl http://20.76.184.112:80/api/v1/service/lr-prod/score -H 'Authorization: Bearer dg3L4Ld98LpNbD4vpzzgLVuOsvgOn3hM' -H 'Content-Type: application/json; format=pandas-split' -d '{"columns":["B1", "B2", "B3"], "data":[[1, 2, 3]]}'
echo ""