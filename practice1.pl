sub validate_password {
    my ($password) = @_;

    # Check length
    my $length = length($password);
    return 0 if $length < 8;

    # Check complexity based on length
    if ($length >= 8 && $length <= 11) {
        return 1 if $password =~ /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,11}$/;
    } elsif ($length >= 12 && $length <= 15) {
        return 1 if $password =~ /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{12,15}$/;
    } elsif ($length >= 16 && $length <= 19) {
        return 1 if $password =~ /^(?=.*[a-z])(?=.*[A-Z])[A-Za-z]{16,19}$/;
    } else {
        return 1;
    }

    return 0; # Default to fail
}

# Example usage:
my $password = "MyPassw0rd!";
if (validate_password($password)) {
    print "Password is valid!\n";
} else {
    print "Password is not valid!\n";
}
