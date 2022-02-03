class MovieC {
    public static function movie(card: Int, ticket: Int, percent: Float): Int {
        var costA = 0;
        var costB = cast (card, Float);
        var i = 0;
        var price = cast (ticket, Float);

        while (costA <= Math.ceil(costB)) {
            costA += ticket;
            costB += price;

            price *= percent;

            i++;
        }

        return i - 1;
    }
}