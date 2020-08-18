import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.page.html',
  styleUrls: ['./user-page.page.scss'],
})
export class UserPagePage implements OnInit {
  loginURL: string;
  logoutURL: string;
  user: string;
  mainText: string;

  constructor(public auth: AuthService) {
    this.loginURL = auth.build_login_link('/tabs/user-page');
    this.logoutURL = auth.build_logout_link();

  }

  ngOnInit() {
    const { permissions }  = this.auth.payload;
    // Check to see if permissions is > than 1 (Manager)
    if(permissions.length > 1) {
      this.user = 'Manager';
      this.mainText = `
            As the Manager of Uda-Spice Latte Cafe, you have
            ability to create, edit, delete and see ingredients
            of drinks. Any recommended drink or updates to the
            application has to get approved by you first.
      `;
      // If permissions = 1 (Barista)
    } else if(permissions.length === 1) {
      this.user = 'Barista';
      this.mainText = `
            As the Barista of Uda-Spice Latte Cafe, you have
            ability to see the ingredients of all drinks. With
            this privilege, you are able to see what it takes
            to make some of our incredible drinks!
      `;
      // Student (Default)
    } else {
      this.user = 'Student';
      this.mainText = `
            Hello there prospect Student! Start your day off right
            by enjoying some of our greatest cup of coffee. Have a
            project due? Is the deadline getting late ? Well have a
            cup of coffee from Uda-Spice today and start coding!
      `;
    }
  }
}
