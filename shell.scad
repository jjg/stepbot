// basic shell
deck_diameter = 125;
wheel_opening_length = 70;
wheel_opening_width = 18;
wheel_center_above_deck = 10;

difference(){

	// outer shell
	sphere(r=deck_diameter / 2,$fn=100);

	// inner shell cut-out
	sphere(r=(deck_diameter / 2) -2,$fn=100);

	// bottom cut-out
	translate([-deck_diameter / 2,-deck_diameter / 2,-deck_diameter]){
		cube([deck_diameter,deck_diameter,deck_diameter]);
	}

	// make sure there's enough room for the wheels in motors-up arrangement
	translate([-(deck_diameter/4)-wheel_opening_width,0,wheel_center_above_deck]){
		rotate([0,90,0]){
				#cylinder(r=wheel_opening_length / 2,h=wheel_opening_width,$fn=100);
			}
	}
	translate([(deck_diameter/4),0,wheel_center_above_deck]){
			rotate([0,90,0]){
				#cylinder(r=wheel_opening_length / 2,h=wheel_opening_width,$fn=100);
			}
	}
}