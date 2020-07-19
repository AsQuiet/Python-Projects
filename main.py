
class Super():

    def should_open_window(self, heavy_rain=False, sick=False, curtain_closed=False):
        return not(heavy_rain or sick or curtain_closed)
    
    def probability(self, reward, penalty, odds_of_reward):
        """Odds of reward between 0 and 1."""

        reward_ = reward * odds_of_reward
        penalty_ = penalty * (1-odds_of_reward)
        ex_value = reward_ - penalty_

        print('expected value is ('+ ("+" if ex_value >= 0 else '-')+ str(round(ex_value)) + '€)')
        return ex_value > 0



s = Super()

print(s.probability(1200, 200, 0.28))
print(s.probability(1200, 450, 0.68))

