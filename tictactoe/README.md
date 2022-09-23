### Underwriting Failure codes

- When underwriting fails, a code is returned. 

| Failure reason    | Details                                                          | Code |
|-------------------|------------------------------------------------------------------|------|
| `age`             | Age of the driver                                                | FR01 |
| `car`             | Car does not match clearance level from Cassie or car is too old | FR02 |
| `cassie_driver`   | Driver rejected by Cassie                                        | FR03 |
| `cassie_owner`    | Owner rejected by cassie                                         | FR04 |
| `cassie_payment`  | Payment rejected by cassie                                       | FR05 |
| `clm`             | Number of claims or convictions too high                         | FR06 |
| `cne`             | This car is not in the allowed list                              | FR07 |
| `same_details`    | The same details have been provided for the owner and driver     | FR08 |
| `equifax`         | Rejected by Equifax                                              | FR09 |
| `ins`             | Car not insured                                                  | FR10 |
| `lic`             | Invalid Licence for the car                                      | FR11 |
| `ldp_with_claims` | Learner driver with claims or convictions is not allowed to buy  | FR12 |
| `licence_exists`  | This licence already exists                                      | FR13 |
| `myl`             | Rejected by My Licence                                           | FR14 |
| `nfi`             | Not finished                                                     | FR15 |
| `pricing`         | Pricing returned None                                            | FR16 |
| `max alf`         | Aggregate Loading Factor was greater than MAX ALF                | FR17 |
| `prov`            | Full provisional not confirmed                                   | FR18 |
| `pss`             | Passed                                                           | pss  |
| `rel`             | Relationship not allowed                                         | FR20 |
| `win`             | Restricted period                                                | FR21 |
| `road_tax`        | Road Tax Expired                                                 | FR22 |
| `mot`             | MOT Expired                                                      | FR23 |
| `max_policies`    | Would exceed max live policies                                   | FR24 |
