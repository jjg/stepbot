deck_diameter = 125;
deck_thickness = 5;
wheel_opening_length = 70;
wheel_opening_width = 18;
motor_diameter = 30;
motor_flange = 45;
motor_mount_width = 10;
motor_shaft_offset = 5;
motor_screw_hole = 4;
motor_screw_offset = 3.5;

difference(){

	union(){
		// main deck
		cylinder(r=deck_diameter / 2,h=deck_thickness);

		// motor mounts
		translate([-(deck_diameter/4)+motor_shaft_offset,-motor_flange/2,deck_thickness]){
			difference(){
				cube([motor_mount_width,motor_flange,motor_diameter*.65]);
				translate([-1,motor_flange/2,motor_diameter/2]){
					rotate([0,90,0]){
						#cylinder(r=motor_diameter/2,h=12);
						translate([0,(motor_diameter/2) + motor_screw_offset,0]){
							#cylinder(r=motor_screw_hole/2,h=motor_mount_width+2);
						}
						translate([0,-(motor_diameter/2) - motor_screw_offset,0]){
							#cylinder(r=motor_screw_hole/2,h=motor_mount_width+2);
						}
					}
				}
			}
		}
		translate([((deck_diameter/4)-motor_mount_width)-motor_shaft_offset,-motor_flange/2,deck_thickness]){
			difference(){
				cube([motor_mount_width,motor_flange,motor_diameter*.65]);
				translate([-1,motor_flange/2,motor_diameter/2]){
					rotate([0,90,0]){
						#cylinder(r=motor_diameter/2,h=12);
						translate([0,(motor_diameter/2) + motor_screw_offset,0]){
							#cylinder(r=motor_screw_hole/2,h=motor_mount_width+2);
						}
						translate([0,-(motor_diameter/2) - motor_screw_offset,0]){
							#cylinder(r=motor_screw_hole/2,h=motor_mount_width+2);
						}
					}
				}
			}
		}
	}

	// wheel openings
	translate([-(deck_diameter/4)-wheel_opening_width,-wheel_opening_length/2,-1]){
		cube([wheel_opening_width, wheel_opening_length, 10]);
	}
	translate([(deck_diameter/4),-wheel_opening_length/2,-1]){
		cube([wheel_opening_width, wheel_opening_length, 10]);
	}
}