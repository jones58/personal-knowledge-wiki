function checkCashRegister(price, cash, cid) {
  const currencyUnit = [
    ["PENNY", 0.01],
    ["NICKEL", 0.05],
    ["DIME", 0.1],
    ["QUARTER", 0.25],
    ["ONE", 1],
    ["FIVE", 5],
    ["TEN", 10],
    ["TWENTY", 20],
    ["ONE HUNDRED", 100],
  ];
  // get difference between price and cash //
  let changeNeeded = cash - price;

  // total amount in cash register //

  let cashTotal = 0;
  for (let i = 0; i < cid.length; i++) {
    cashTotal += cid[i][1];
  }
  cashTotal = Number(cashTotal.toFixed(2));

  let AnswerObject = {
    status: "",
    change: [],
  };

  if (cashTotal >= changeNeeded) {
    // run through cid from end to start
    for (let i = 8; i >= 0; i--) {
      if (currencyUnit[i][1] > changeNeeded) {
        continue;
      } else if (cid[i][1] > 0) {
        let changeDue =
          Math.floor(
            Math.min(changeNeeded, cid[i][1]) / currencyUnit[i][1]
          ) * currencyUnit[i][1];
        AnswerObject.change.push([currencyUnit[i][0], changeDue]);
        changeNeeded -= changeDue;
        changeNeeded = Number(changeNeeded.toFixed(2));
        cashTotal -= changeDue;
      } else if (cid[i][1] === changeNeeded) {
        let changeDue =
          (changeNeeded / currencyUnit[i][1]) * currencyUnit[i][1];
        AnswerObject.status = "CLOSED";
        AnswerObject.change = cid;
        changeNeeded -= changeDue;
        cashTotal -= changeDue;
      }
    }
  }
  if (changeNeeded > 0) {
    AnswerObject.status = "INSUFFICIENT_FUNDS";
    AnswerObject.change = [];
  } else if (changeNeeded === 0 && cashTotal > 0) {
    AnswerObject.status = "OPEN";
  } else if (cashTotal === 0) {
    AnswerObject.status = "CLOSED";
    AnswerObject.change = cid;
  }

  return AnswerObject;
}
