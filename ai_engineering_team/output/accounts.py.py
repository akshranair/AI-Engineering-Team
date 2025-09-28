class Account:
    def __init__(self, username: str, email: str, password: str) -> None:
        """
        Initializes a new Account instance.

        Args:
            username (str): Unique username for the account.
            email (str): Valid email address associated with the account.
            password (str): Secure password for the account.
        """
        self.username = username
        self.email = email
        self.password = password
        self.active = True

    def update_email(self, new_email: str) -> None:
        """
        Updates the email address associated with the account.

        Args:
            new_email (str): New email address to be set.

        Raises:
            ValueError: If the new email format is invalid.
        """
        if '@' not in new_email or '.' not in new_email.split('@')[-1]:
            raise ValueError("Invalid email format.")
        self.email = new_email

    def update_password(self, new_password: str) -> None:
        """
        Updates the password for the account.

        Args:
            new_password (str): New password to set for the account.

        Raises:
            ValueError: If the new password does not meet the security requirements.
        """
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        self.password = new_password

    def get_account_info(self) -> dict:
        """
        Returns the account information.

        Returns:
            dict: A dictionary containing `username`, `email`, and an indication of whether the account is active or not.
        """
        return {
            'username': self.username,
            'email': self.email,
            'active_status': self.active
        }

    def deactivate_account(self) -> None:
        """
        Marks the account as inactive.
        """
        self.active = False

    def activate_account(self) -> None:
        """
        Reactivates the account if it was previously deactivated.
        """
        self.active = True