use strict;
use warnings;
use Test::More;

sub validate_password {
    my ($password) = @_;

    # Check length
    my $length = length($password);
    return 0 if $length < 8;

    # Check complexity based on length
    if ($length >= 8 && $length <= 11) {
        return 1 if $password =~ /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,11}$/;
    } elsif ($length >= 12 && $length <= 15) {
        return 1 if $password =~ /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{12,15}$/;
    } elsif ($length >= 16 && $length <= 19) {
        return 1 if $password =~ /^(?=.*[a-z])(?=.*[A-Z])[A-Za-z]{16,19}$/;
    } else {
        return 1;
    }

    return 0; # Default to fail
}

# Test cases
my @test_cases = (
    # Valid passwords
    { password => "MyPassw0rd!", expected_result => 1 },
    { password => "StrongPasswordabc", expected_result => 1 },
    { password => "SecurePwd!123", expected_result => 1 },
    # Invalid passwords
    { password => "weakpwd", expected_result => 0 },
    { password => "onlyletters", expected_result => 0 },
    { password => "12345678", expected_result => 0 },
    { password => "noSymbol123", expected_result => 0 },
    { password => "noUpperCase123@", expected_result => 0 },
    { password => "NoLowerCase@", expected_result => 0 },
);

# Run tests
plan tests => scalar @test_cases;

foreach my $test_case (@test_cases) {
    my $password = $test_case->{password};
    my $expected_result = $test_case->{expected_result};
    my $result = validate_password($password);
    is($result, $expected_result, "Password '$password' validation");
}

done_testing();
