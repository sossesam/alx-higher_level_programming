exports.converter = function (base) {
  function convert (number, base) {
    let convertedNumber = '';
    while (number) {
      const remainder = number % base;
      convertedNumber = remainder + convertedNumber;
      number = Math.floor(number / base);
    }
    return convertedNumber;
  }

  return function (number) {
    return convert(number, base);
  };
};
