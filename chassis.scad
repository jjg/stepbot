deck_diameter = 150;
wheel_opening_length = 70;
wheel_opening_width = 15;

difference(){

	union(){
		// main deck
		cylinder(r=deck_diameter / 2,h=5);

		// motor mounts
	}

	// wheel openings
	translate([-(deck_diameter/4)-wheel_opening_width,-wheel_opening_length/2,-1]){
		cube([wheel_opening_width, wheel_opening_length, 10]);
	}
	translate([(deck_diameter/4),-wheel_opening_length/2,-1]){
		cube([wheel_opening_width, wheel_opening_length, 10]);
	}
}