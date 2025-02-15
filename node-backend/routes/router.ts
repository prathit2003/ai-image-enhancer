import express from "express";
import imageenhanceRouter from "./imageenhance";
import backgroundremoverRouter from "./backgroundremover";
import formatchangerRouter from "./formatchanger";
import imageeditrouter from "./imageediting";
const router = express.Router();

router.use("/imageenhance", imageenhanceRouter);
router.use("/backgroundremover", backgroundremoverRouter);
router.use("/formatchanger", formatchangerRouter);
router.use("/imageedit", imageeditrouter );

export default router;
