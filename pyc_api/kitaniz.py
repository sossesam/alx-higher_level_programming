 Registration:
		IF Registraction:
			IS Tokunbo OR Naija Used:
				IF Tokunboh:
					Cost <--- 75,000 naira
					Name of owner <-----(input)
                    Address of owner <-----(input)
                    Phone number of owner <-----(input)
                    Make and Model of vehicle <-----(input)
                    Color <-----(input)
                    Engine number <-----(input)
                    Chasis number <-----(input)

                    return vehicle license, Road worthiness, insurance, plate number, proof of ownership, allocation paper.

                Else IF Naija used:
                    IS vehicle license valid:
                            IF false:
                                renew till valid
                            Else:
                                Cost <----- 90,000
                                Name of owner <-----(input)
                                Address of owner <-----(input)
                                Phone number of owner <-----(input)
                                Make and Model of vehicle <-----(input)
                                Color <-----(input)
                                Engine number <-----(input)
                                Chasis number <-----(input)
                                vehicle license OR ALLocation papers OR Proof of ownership = true:

                                return vehicle license, Road worthiness, insurance, plate number, proof of ownership, allocation paper.
